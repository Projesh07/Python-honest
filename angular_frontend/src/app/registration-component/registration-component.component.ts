import { Component, OnInit } from '@angular/core';
import {RegisterUser} from '../campaign-model';
import {CampaignService} from '../campaign.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-registration-component',
  templateUrl: './registration-component.component.html',
  styleUrls: ['./registration-component.component.css']
})
export class RegistrationComponentComponent implements OnInit {

  constructor(private userEnter: CampaignService,private activatedRoute: ActivatedRoute) { }

  users: RegisterUser[] = [];
  counter = 0;
  user: RegisterUser;
  message="";

  errorList =[];

  ngOnInit() {
  }

    onSubmit(value) { 
    this.user = new RegisterUser(value.username, value.email, value.password1,value.password2);
    if(value) {
      this.users.push(this.user);

    }
    console.log(this.user);
    this.postRegister(this.user);
    console.log(this.users);
    this.counter++;
  }


  postRegister(id): void {
    this.userEnter.postRegister(id)
        .subscribe(
        users=> {
          this.users = users;
          console.log(this.users);
         
        },
        (errorData) => {
                 // Error callback
                 var error = errorData.json();
                 console.log(error);
                
                for (let key in error) {
                      var values = error[key];
                      for(let obj of values){
                          this.errorList.push(obj);
                      }
                      
                }
                console.log(this.errorList);

                }
             );
  }

}
