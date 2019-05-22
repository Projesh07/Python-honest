import { Component, OnInit,Input,OnChanges } from '@angular/core';

@Component({
  selector: 'app-medium-category-item',
  templateUrl: './medium-category-item.component.html',
  styleUrls: ['./medium-category-item.component.css']
})
export class MediumCategoryItemComponent implements OnInit,OnChanges {

  @Input("categoryId") categoryId;
  @Input("categoryName") categoryName;
  @Input("categoryImgSrc") categoryImgSrc;
  @Input("selectedCategory") selectedCategory;
  selected=false;
  constructor() { }

  ngOnInit() {
  }

  ngOnChanges(){
    if(this.selectedCategory==this.categoryId){
      this.selected=true;
    }
  }

}
