import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from "@angular/router"
import {CampaignService} from './../../services/campaign.service';
import {CategorylistService} from './../../services/categorylist.service';
import {Campaign} from './../../models/campaign';
import {environment} from '../../../environments/environment';
import {Category} from "../../models/category";
import {CampaignList} from "../../models/campaignlist";
@Component({
  selector: 'app-campaigns',
  templateUrl: './campaigns.component.html',
  styleUrls: ['./campaigns.component.css'],
  providers:[CampaignService,CategorylistService]
})
export class CampaignsComponent implements OnInit {

  photobaseUrl=environment.photo_base_url;
  campaigns:Campaign[];
  campaignList:CampaignList;
  categoryId:number;
  limit = 6;
  offset = 0;
  currentPage = 1;

  constructor(private campaignService:CampaignService,private route: ActivatedRoute,private categorylistService:CategorylistService) {

  }

  ngOnInit() {
    this.route.params.subscribe(
        params => {
            if(params['categoryId']){
              this.categoryId = params['categoryId'];
              this.getCampaignsByCategoryId(params['categoryId']);
            }else{
              this.getCampaigns();
            }
        }
    );

  }

  getCampaigns(){
    this.campaignService.getCampaigns(this.limit,this.offset).subscribe(
      (data)=>{
        this.campaignList=data;
      },
      (err)=>{
        console.log(err);
      }
    );
  }

  getCampaignsByCategoryId(categoryId){
    this.campaignService.getCampaignsByCategoryId(categoryId,this.limit,this.offset).subscribe(
      (data)=>{
        this.campaignList=data;
      },
      (err)=>{
        console.log(err);
      }
    );
  }

  pageChanged(pageNumber){
    this.offset = (pageNumber * this.limit) - this.limit;
    this.currentPage = pageNumber;
    if(this.categoryId){
      this.getCampaignsByCategoryId(this.categoryId);
    }else{
      this.getCampaigns();
    }
  }

}
