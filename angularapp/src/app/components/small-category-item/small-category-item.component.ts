import { Component, OnInit , Input } from '@angular/core';

@Component({
  selector: 'app-small-category-item',
  templateUrl: './small-category-item.component.html',
  styleUrls: ['./small-category-item.component.css']
})
export class SmallCategoryItemComponent implements OnInit {
  @Input("categoryId") categoryId;
  @Input("categoryName") categoryName;
  @Input("categoryImgSrc") categoryImgSrc;
  constructor() { }

  ngOnInit() {
  }

}
