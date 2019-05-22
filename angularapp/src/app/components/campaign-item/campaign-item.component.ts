import { Component, OnInit,Input } from '@angular/core';

@Component({
  selector: 'app-campaign-item',
  templateUrl: './campaign-item.component.html',
  styleUrls: ['./campaign-item.component.css']
})
export class CampaignItemComponent implements OnInit {

  @Input("campaignFeaturedImgSrc") campaignFeaturedImgSrc;
  @Input("campaignTitle") campaignTitle;
  @Input("campaignShortDesc") campaignShortDesc;
  @Input("campaignProgress") campaignProgress:number;
  @Input("campaignRaisedAmount") campaignRaisedAmount;
  @Input("campaignGoalAmount") campaignGoalAmount;
  @Input("campaignSlug") campaignSlug;
  @Input("slick") slick : boolean=false;
  constructor() { }

  ngOnInit() {
  }

}
