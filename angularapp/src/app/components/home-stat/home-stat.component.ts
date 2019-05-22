import { Component, OnInit } from '@angular/core';
import {ReportService} from '../../services/report.service';
import {HomeStat} from '../../models/homestat';
@Component({
  selector: 'app-home-stat',
  templateUrl: './home-stat.component.html',
  styleUrls: ['./home-stat.component.css'],
  providers:[ReportService]
})
export class HomeStatComponent implements OnInit {

  homeStat :HomeStat;

  constructor(private reportService:ReportService) { }

  ngOnInit() {
    this.getHomeStatatistics();
  }

  getHomeStatatistics(){
    this.reportService.getHomeStat().subscribe(
      (data)=>{
        this.homeStat = data;
      },(err)=>{
        console.log(err);
      }
    );
  }
}
