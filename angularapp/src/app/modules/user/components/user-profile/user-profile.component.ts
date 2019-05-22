import { Component, OnInit } from '@angular/core';
import {UserService} from "../../../../services/user.service";
import {UserDetails} from "../../../../models/user-details";
import {NgForm} from '@angular/forms'
import * as $ from 'jquery';
@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent implements OnInit {
  user:UserDetails;
  edit=false;
  firstname:string;
  lastname:string;
  constructor(private userService:UserService) { }

  ngOnInit() {
    this.userService.details().subscribe(
      (data)=>{
        this.user=data;
        this.firstname=data.first_name;
        this.lastname=data.last_name;
      }
    );
  }
  enableEdit(){
    this.edit=true;
  }
  disableEdit(){
    this.edit=false;
  }
  updateInfo(f: NgForm){
    if(f.valid){
      const firstName = f.value.firstName;
      const lastName = f.value.lastName;
      this.userService.update(firstName,lastName).subscribe(
        (data)=>{
          this.firstname=data.first_name;
          this.lastname=data.last_name;
          this.edit=false;
          this.user.first_name=data.first_name;
          this.user.last_name=data.last_name;
          $('.user-name').html(this.firstname+' '+this.lastname);
        }
      );

    }

  }
}
