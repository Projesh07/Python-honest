import { Component, OnInit,Input,OnChanges } from '@angular/core';
import {CategorylistService} from './../../services/categorylist.service';
import {Campaign} from './../../models/campaign';
import {environment} from '../../../environments/environment';
import {Category} from "../../models/category";

@Component({
  selector: 'app-cover-banner',
  templateUrl: './cover-banner.component.html',
  styleUrls: ['./cover-banner.component.css'],
  providers:[CategorylistService]
})
export class CoverBannerComponent implements OnInit,OnChanges {

  @Input("categoryId") categoryId;

  photobaseUrl=environment.photo_base_url;
  category:Category;
  bannerImg = "assets/img/charity.jpg";
  tagline = "HELP PEOPLE";
  categoryName="All";
  constructor(private categorylistService:CategorylistService) { }

  ngOnInit() {
    //this.getCategoryDetails(this.categoryId);
  }

  ngOnChanges(){
    if(this.categoryId){
      this.getCategoryDetails(this.categoryId);
    }

  }

  getCategoryDetails(id){
    console.log("cover");
    this.categorylistService.getCategoryDetails(id).subscribe(
      (data)=>{
        this.category=data;
        this.bannerImg = this.photobaseUrl+this.category.cover_photo_url;
        this.tagline=this.category.tagline;
        this.categoryName = this.category.name;
      }
    );
  }

}
