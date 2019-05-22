import { Component, OnInit , Input } from '@angular/core';

@Component({
  selector: 'app-campaign-countdown',
  templateUrl: './campaign-countdown.component.html',
  styleUrls: ['./campaign-countdown.component.css']
})
export class CampaignCountdownComponent implements OnInit {

  @Input("endAt") endAt;
  constructor() { }

  ngOnInit() {
  }

}
