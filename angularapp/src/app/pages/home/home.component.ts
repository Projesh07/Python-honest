import { Component, OnInit,ViewChild } from '@angular/core';
import * as $ from 'jquery';
import { Meta } from '@angular/platform-browser';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],

})
export class HomeComponent implements OnInit {
  @ViewChild('slickModal') slickModal;
  slideConfig = {"slidesToShow": 3, "slidesToScroll": 3,prevArrow:$('.prev-people'),
        nextArrow: $('.next-people')};
  constructor(private meta: Meta) {
    this.meta.addTag({ name: 'description', content: 'CHARITY IS THE BEST FORM OF PRAYER'});
    this.meta.addTag({ name: 'keywords', content: 'Donation,Charity,help'});
  }

  ngOnInit() {

  }
  afterChange(e) {
    console.log('afterChange');
  }

  slickNext(e){
    this.slickModal.slickNext();
  }
  slickPrev(e){
    this.slickModal.slickPrev();
  }


}
