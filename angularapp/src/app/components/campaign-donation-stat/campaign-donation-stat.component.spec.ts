import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CampaignDonationStatComponent } from './campaign-donation-stat.component';

describe('CampaignDonationStatComponent', () => {
  let component: CampaignDonationStatComponent;
  let fixture: ComponentFixture<CampaignDonationStatComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CampaignDonationStatComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CampaignDonationStatComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
