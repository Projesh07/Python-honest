import { Component, OnInit } from '@angular/core';
import {UserService} from "../../../../services/user.service";
import {UserDonationStat} from "../../../../models/user-donation-stat";

@Component({
  selector: 'app-user-dashboard-stat',
  templateUrl: './user-dashboard-stat.component.html',
  styleUrls: ['./user-dashboard-stat.component.css']
})
export class UserDashboardStatComponent implements OnInit {

  userDonationStat:UserDonationStat;
  constructor(private userService:UserService) { }

  ngOnInit() {
    this.userService.stat().subscribe(
      (data)=>{
        this.userDonationStat=data;
      }
    );
  }

}
