import { Component,OnInit } from '@angular/core';
import {LoadingBarService} from '@ngx-loading-bar/core';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  loadingBarColor = '#42B77A';
  //constructor(public loader: LoadingBarService) {}

  ngOnInit(){
    console.log("app");
  }

}
