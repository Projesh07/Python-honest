import { Component, OnInit,OnChanges } from '@angular/core';
import {ActivatedRoute,Router, NavigationEnd} from "@angular/router";
import {CampaignService} from './../../services/campaign.service';
import {CampaignDetails} from './../../models/campaign-details';
import {CommentList} from '../../models/commentlist';
import {environment} from '../../../environments/environment';
import { Observable } from 'rxjs/Observable';
import {NgForm} from '@angular/forms'
import {AuthenticaionService} from "./../../services/authenticaion.service";
import * as $ from 'jquery';
@Component({
  selector: 'app-campaign-details',
  templateUrl: './campaign-details.component.html',
  styleUrls: ['./campaign-details.component.css'],
  providers:[CampaignService]
})
export class CampaignDetailsComponent implements OnInit,OnChanges {
  isLoggedIn$:Observable<boolean>;
  photobaseUrl=environment.photo_base_url;
  slug:string;
  campaign:CampaignDetails;
  campaignID:number;
  coverImgUrl:string;
  coverVdoUrl:string=null;
  isVdoAvailable=false;
  images:string[]=[];
  vedios:string[]=[];
  links:string[]=[];
  comments:CommentList;
  limit = 5;
  offset = 0;
  currentPage = 1;
  constructor(private route: ActivatedRoute,private campaignService:CampaignService,private authenticationService:AuthenticaionService) { }

  ngOnInit() {
    $("#first_tab").click(function() {
        $("#tri").css("left", "12%");
    });
    $("#second_tab").click(function() {
        $("#tri").css("left", "50%");
    });
    $("#third_tab").click(function() {
        $("#tri").css("left", "84%");
    });
    this.route.params.subscribe(
        params => {
            if(params['slug']){
              this.slug = params['slug'];
              window.scrollTo(0, 0);
            }
        }
    );
    this.getCampaignDetails();
    this.isLoggedIn$ = this.authenticationService.isLoggedIn;
  }

  getCampaignDetails(){
    const thisComponent = this;
    this.campaignService.getCampaignDetails(this.slug).subscribe(
      (data)=>{
        this.campaign=data;
        this.campaignID = data.id;
        this.campaign.documents.forEach(
          function(item){
            if(item.content_type === "cover_image"){
                thisComponent.coverImgUrl = item.content;
                thisComponent.images.push(item.content_resized);
            }
            if(item.content_type === "cover_video_link"){
                thisComponent.coverVdoUrl = "https://www.youtube.com/embed/"+item.content;
                thisComponent.isVdoAvailable=true;
                thisComponent.vedios.push("https://www.youtube.com/embed/"+item.content);
            }
            if(item.content_type==="image"){
              thisComponent.images.push(item.content_resized)
            }
            if(item.content_type==="videolink"){
              thisComponent.vedios.push("https://www.youtube.com/embed/"+item.content);
            }
            if(item.content_type=="link"){
              thisComponent.links.push(item.content);
            }

          }
        );
        this.getCommentsOfCampaign();
      }
    );

  }
  ngOnChanges(){
    console.log("herer");

  }
  getCommentsOfCampaign(){
    if(this.campaignID){
      this.campaignService.getComments(this.campaignID,this.limit,this.offset).subscribe(
      (data)=>{
        this.comments=data;
        this.comments.results.forEach(
          function(item){
            if(item.user.profile.image_url!=null){
              if(item.user.profile.image_url.startsWith("http://graph.facebook.com"))
              {
                item.user.profile.image_url=item.user.profile.image_url;
              }else if(item.user.profile.image_url.startsWith("https://lh3.googleusercontent.com")){
                 item.user.profile.image_url=item.user.profile.image_url;
              }else{
                item.user.profile.image_url=environment.photo_base_url+"/"+item.user.profile.image_url;
              }
            }
          }
        );
      }
    )
    }

  }

  postComment(f: NgForm){
    if(f.valid){
      const reply = f.value.reply;
      this.campaignService.postComment(this.campaignID,reply).subscribe(
        (data)=>{
          this.comments.results.unshift(data);
          f.reset();
        }
      )
    }

  }
  pageChanged(pageNumber){
    this.offset = (pageNumber * this.limit) - this.limit;
    this.currentPage = pageNumber;
    this.getCommentsOfCampaign();
  }

}
