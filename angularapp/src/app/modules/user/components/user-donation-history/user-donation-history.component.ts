import { Component, OnInit } from '@angular/core';
import {UserService} from "../../../../services/user.service";
import {Donate} from "../../../../models/donate";

@Component({
  selector: 'app-user-donation-history',
  templateUrl: './user-donation-history.component.html',
  styleUrls: ['./user-donation-history.component.css']
})
export class UserDonationHistoryComponent implements OnInit {

  donations:Donate[];
  constructor(private userService:UserService) { }

  ngOnInit() {
    this.userService.donations().subscribe(
      (data)=>{
        this.donations=data;
      }
    );
  }

}
