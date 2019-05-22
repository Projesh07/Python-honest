import { Component, OnInit,Input,OnChanges } from '@angular/core';
import {ReportService} from './../../services/report.service';
import {CampaignStat} from './../../models/campaign-stat';
@Component({
  selector: 'app-campaign-donation-stat',
  templateUrl: './campaign-donation-stat.component.html',
  styleUrls: ['./campaign-donation-stat.component.css'],
  providers:[ReportService]
})
export class CampaignDonationStatComponent implements OnChanges {

  @Input("campaignId") campaignId;
  campaignStat:CampaignStat;

  constructor(private reportService:ReportService) { }

  ngOnChanges() {
    if(this.campaignId){
      this.reportService.getDonationStat(this.campaignId).subscribe(
      (data)=>{
        this.campaignStat = data;
      }
    )
    }

  }

}
