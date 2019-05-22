import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CampaignProgressBarComponent } from './campaign-progress-bar.component';

describe('CampaignProgressBarComponent', () => {
  let component: CampaignProgressBarComponent;
  let fixture: ComponentFixture<CampaignProgressBarComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CampaignProgressBarComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CampaignProgressBarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
