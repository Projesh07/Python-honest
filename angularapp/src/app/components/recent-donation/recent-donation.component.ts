import { Component, OnInit,Input,OnChanges } from '@angular/core';
import {CampaignService} from "../../services/campaign.service";
import {Donate} from "../../models/donate";
import {environment} from '../../../environments/environment';
@Component({
  selector: 'app-recent-donation',
  templateUrl: './recent-donation.component.html',
  styleUrls: ['./recent-donation.component.css'],
  providers:[CampaignService]
})
export class RecentDonationComponent implements OnInit,OnChanges {

  @Input("campaignId") campaignId;
  donations:Donate[];
  photobaseUrl=environment.photo_base_url;
  constructor(private campaignService:CampaignService) { }

  ngOnInit() {

  }
  ngOnChanges(){
    if(this.campaignId){
      this.campaignService.getRecentDonation(this.campaignId).subscribe(
        (data)=>{
          this.donations = data;
          this.donations.forEach(
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

}
