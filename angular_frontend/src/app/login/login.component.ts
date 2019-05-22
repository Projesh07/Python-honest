import { Component, OnInit } from '@angular/core';

import {LoginUser} from '../campaign-model';
import {AuthService} from '../auth.service';
import { ActivatedRoute,Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(private userEnter: AuthService,private activatedRoute: ActivatedRoute,private router: Router) { }

  users: LoginUser[] = [];
  counter = 0;
  user: LoginUser;
  message="";

  errorList =[];


  ngOnInit() {
  }

     onSubmit(value) { 
    this.user = new LoginUser(value.username,value.password);
    if(value) {
      this.users.push(this.user);

    }
    console.log(this.user);
    this.login(this.user);
    console.log(this.users);
    this.counter++;
  }

    login(user): void {
    this.userEnter.login(user)
        .subscribe(
        users=> {
          this.users = users;
          console.log(this.users);

          this.router.navigate(['user-profile']);
         
        },
        (errorData) => {
                 // Error callback
                 console.log(errorData);
                 var error = errorData.json();
                 console.log(error+"ok");
                
                for (let key in error) {
                      var values = error[key];
                 
                      for(let obj of values){
                          this.errorList.push(obj);
                      }
                      
                }
                console.log(this.errorList+"hello");

                }
             );
  }

}
