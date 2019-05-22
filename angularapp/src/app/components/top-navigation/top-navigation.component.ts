import { Component,OnInit, OnChanges,AfterViewChecked,AfterViewInit } from '@angular/core';
import {AuthenticaionService} from "../../services/authenticaion.service";
import { Observable } from 'rxjs/Observable';
import {Router,ActivatedRoute} from "@angular/router"
@Component({
  selector: 'app-top-navigation',
  templateUrl: './top-navigation.component.html',
  styleUrls: ['./top-navigation.component.css'],
  providers:[AuthenticaionService]
})
export class TopNavigationComponent implements OnInit,AfterViewChecked,AfterViewInit {
  isLoggedIn$:Observable<boolean>;
  returnUrl: string;
  constructor(private router: Router,private route: ActivatedRoute,private authenticationService:AuthenticaionService) {}

  ngOnInit() {
    this.isLoggedIn$ = this.authenticationService.isLoggedIn;
    this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
  }
  logout(){
    this.authenticationService.logout();
    this.router.navigate(['/']);
  }
  ngAfterViewChecked(){
      //console.log("called after view checked");
      this.isLoggedIn$ = this.authenticationService.isLoggedIn;
   }
  ngAfterViewInit(){
    console.log("called init");
    //this.isLoggedIn$ = this.authenticationService.isLoggedIn;

  }
}
