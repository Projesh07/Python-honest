import { Component, OnInit } from '@angular/core';
import {Router,ActivatedRoute} from "@angular/router"
import { User } from '../../models/user';
import { AuthenticaionService } from '../../services/authenticaion.service';
import {
    AuthService,
    FacebookLoginProvider,
    GoogleLoginProvider
} from 'angular5-social-login';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  submitted = false;

  loading = false;
  model = new User();
  returnUrl: string;

  constructor(private socialAuthService: AuthService,private router: Router,private route: ActivatedRoute,private authenticationService: AuthenticaionService) { }

  ngOnInit() {
    // reset login status
    this.authenticationService.logout();

    // get return url from route parameters or default to '/'
    this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
  }

  onSubmit() { this.submitted = true; }

  login() {
    this.loading = true;
    this.authenticationService.login(this.model.username, this.model.password)
        .subscribe(
            data => {
              this.router.navigate([this.returnUrl]);
            },
            error => {
                console.log('not authenticated')
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
              this.router.navigate([this.returnUrl]);
            },
            error=> {
              console.log('not authenticated')
              this.loading = false;
            }
          );
        } else if (socialPlatform == "facebook") {
          this.authenticationService.loginUsingFacebook(userData.token).subscribe(
            (data)=> {
              this.router.navigate([this.returnUrl]);
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
