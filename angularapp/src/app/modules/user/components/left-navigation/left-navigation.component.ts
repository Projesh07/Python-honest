import { Component, OnInit } from '@angular/core';
import {UserService} from "../../../../services/user.service";
import {UserDetails} from "../../../../models/user-details";
import {AuthenticaionService} from "../../../../services/authenticaion.service";
import {Router,ActivatedRoute} from "@angular/router"
import {environment} from '../../../../../environments/environment';
@Component({
  selector: 'app-left-navigation',
  templateUrl: './left-navigation.component.html',
  styleUrls: ['./left-navigation.component.css']
})
export class LeftNavigationComponent implements OnInit {
  photobaseUrl=environment.photo_base_url;
  user:UserDetails;
  constructor(private router: Router,private userService:UserService,private authenticationService:AuthenticaionService) { }
  imageUrl = "assets/img/profile.png";
  isPrivate=false;
  ngOnInit() {
    this.userService.details().subscribe(
      (data)=>{
        this.user=data;
        if(data.profile){
          if(data.profile.image_url!=null){
            if(data.profile.image_url.startsWith("http://graph.facebook.com"))
            {
              this.imageUrl=data.profile.image_url;
            }else if(data.profile.image_url.startsWith("https://lh3.googleusercontent.com")){
              this.imageUrl=data.profile.image_url;
            }else{
              this.imageUrl=this.photobaseUrl+"/"+data.profile.image_url;
            }

          }

          this.isPrivate=data.profile.is_private;
        }
      }
    )
  }
  logout(){
    this.authenticationService.logout();
    this.router.navigate(['/']);
  }

  imageUpload(fileInput){
    if (fileInput.target.files && fileInput.target.files[0]) {
      const file=fileInput.target.files[0];
      this.userService.imageUpload(file).subscribe(
        (data)=>{
          this.imageUrl=this.photobaseUrl+"/"+data.image_url;
        }
      );
    }
  }

  profileVisibility($event){
    this.userService.changeVisibility($event.target.checked).subscribe(
      (data)=>{
        this.isPrivate=data;
      }
    );
  }

}
