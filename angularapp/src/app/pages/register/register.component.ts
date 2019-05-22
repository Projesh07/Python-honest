import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { UserService } from '../../services/user.service';
import { User } from '../../models/user';
import {
    AuthService,
    FacebookLoginProvider,
    GoogleLoginProvider
} from 'angular5-social-login';
import { AuthenticaionService } from '../../services/authenticaion.service';
@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  loading = false;
  model = new User;
  constructor(private socialAuthService: AuthService,private router: Router,private userService: UserService,private authenticationService: AuthenticaionService) { }

  ngOnInit() {
  }

  register() {
    this.loading = true;
    this.userService.creat(this.model)
        .subscribe(
            data => {
                // set success message and pass true paramater to persist the message after redirecting to the login page
                // this.alertService.success('Registration successful', true);
                this.router.navigate(['/login']);
            },
            error => {
                // this.alertService.error(error);
                this.loading = false;
            });
  }

   public socialSignIn(socialPlatform : string) {
    let socialPlatformProvider;
    if(socialPlatform == "facebook"){
      socialPlatformProvider = FacebookLoginProvider.PROVIDER_ID;
    }else if(socialPlatform == "google"){
      socialPlatformProvider = GoogleLoginProvider.PROVIDER_ID;
    }

    this.socialAuthService.signIn(socialPlatformProvider).then(
      (userData) => {
        console.log(userData);
        if (socialPlatform == "google") {
          this.authenticationService.loginUsingGoogle(userData.token).subscribe(
            (data)=> {
              this.router.navigate(['/']);
            },
            error=> {
              console.log('not authenticated')
              this.loading = false;
            }
          );
        } else if (socialPlatform == "facebook") {
          this.authenticationService.loginUsingFacebook(userData.token).subscribe(
            (data)=> {
              this.router.navigate(['/']);
            },
            error=> {
              console.log('not authenticated')
              this.loading = false;
            }
          );
        }
      }
    );
  }

}
