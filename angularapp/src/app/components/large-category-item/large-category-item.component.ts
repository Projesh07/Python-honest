import { Component, OnInit,Input } from '@angular/core';

@Component({
  selector: 'app-large-category-item',
  templateUrl: './large-category-item.component.html',
  styleUrls: ['./large-category-item.component.css']
})
export class LargeCategoryItemComponent implements OnInit {

  @Input("categoryId") categoryId:number;
  @Input("categoryName") categoryName:string;
  @Input("categoryImgSrc") categoryImgSrc:string;
  @Input("categoryShortDesc") categoryShortDesc:string;
  constructor() { }

  ngOnInit() {
  }

}
