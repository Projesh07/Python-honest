import { Component, OnInit,Input,OnChanges } from '@angular/core';
import {ReportService} from './../../services/report.service';
import {HomeStat} from "./../../models/homestat";
@Component({
  selector: 'app-campaigns-stat',
  templateUrl: './campaigns-stat.component.html',
  styleUrls: ['./campaigns-stat.component.css'],
  providers:[ReportService]
})
export class CampaignsStatComponent implements OnInit {

  @Input("categoryId") categoryId;
  stat:HomeStat;

  constructor(private reportService:ReportService) { }

  ngOnInit(){}
  ngOnChanges() {
    if(this.categoryId){
      this.getCategoryStat(this.categoryId);
    }else{
      this.getHomeStat();
    }
  }

  getCategoryStat(id){
    this.reportService.getCategoryStat(id).subscribe(
      (data)=>{
        this.stat=data;
      }
    );
  }

  getHomeStat(){
    this.reportService.getHomeStat().subscribe(
      (data)=>{
        this.stat = data;
      }
    );
  }

}
