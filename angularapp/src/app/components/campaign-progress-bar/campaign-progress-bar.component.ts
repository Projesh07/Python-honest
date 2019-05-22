import { Component, OnInit,Input } from '@angular/core';

@Component({
  selector: 'app-campaign-progress-bar',
  templateUrl: './campaign-progress-bar.component.html',
  styleUrls: ['./campaign-progress-bar.component.css']
})
export class CampaignProgressBarComponent implements OnInit {

  @Input("progress") progress;
  @Input("target") target;
  @Input("raised") raised;
  constructor() { }

  ngOnInit() {
  }

}
