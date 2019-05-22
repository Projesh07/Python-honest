import { Component, OnInit,Input,OnChanges } from '@angular/core';
import {CategorylistService} from '../../services/categorylist.service';
import {Category} from '../../models/category';
import {environment} from '../../../environments/environment';
@Component({
  selector: 'app-medium-category-list',
  templateUrl: './medium-category-list.component.html',
  styleUrls: ['./medium-category-list.component.css'],
  providers:[CategorylistService]
})
export class MediumCategoryListComponent implements OnInit,OnChanges {

  @Input("selectedCategory") selectedCategory;
  categories:Category[];
  categoryName="Categories";
  categoryDesc="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat.";
  photobaseUrl=environment.photo_base_url;

  constructor(private categoryListService:CategorylistService) { }

  ngOnInit() {
    //this.getCategories();
  }
  ngOnChanges(){
    this.getCategories();
    if(this.selectedCategory){
      this.getCategoryDetails();
    }

  }
  getCategories(){
    this.categoryListService.getCategoryList().subscribe(
      (data)=>{
        this.categories=data;
      },
      (err)=>{
        console.log(err);
      }
    );
  }

  getCategoryDetails(){
    this.categoryListService.getCategoryDetails(this.selectedCategory).subscribe(
      (data)=>{
          this.categoryName=data.name;
          this.categoryDesc=data.descriptions;
      }
    );
  }

}
