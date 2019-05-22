import { Component, OnInit } from '@angular/core';
import {CategorylistService} from '../../services/categorylist.service';
import {Category} from '../../models/category';
import {environment} from '../../../environments/environment';
@Component({
  selector: 'app-small-category-list',
  templateUrl: './small-category-list.component.html',
  styleUrls: ['./small-category-list.component.css'],
  providers:[CategorylistService]
})
export class SmallCategoryListComponent implements OnInit {
  categories:Category[];

  photobaseUrl=environment.photo_base_url;
  constructor(private categoryListService:CategorylistService) { }

  ngOnInit() {
    this.getCategories();
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

}
