import { Component, OnInit,Input,OnChanges } from '@angular/core';
import {CampaignService} from "../../services/campaign.service";
import {Campaign} from "../../models/campaign";
import {environment} from '../../../environments/environment';
@Component({
  selector: 'app-related-campaign-list',
  templateUrl: './related-campaign-list.component.html',
  styleUrls: ['./related-campaign-list.component.css'],
  providers:[CampaignService]
})
export class RelatedCampaignListComponent implements OnInit,OnChanges {

  @Input("campaignId") campaignId;
  campaigns:Campaign[];
  photobaseUrl=environment.photo_base_url;
  constructor(private campaignService:CampaignService) { }

  ngOnInit() {
  }
  ngOnChanges(){
    if(this.campaignId){
      this.campaignService.getRelatedCampaigns(this.campaignId).subscribe(
        (data)=>{
          this.campaigns = data;
        }
      );
    }
  }

}
