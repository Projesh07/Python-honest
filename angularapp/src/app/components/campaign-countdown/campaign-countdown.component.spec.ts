import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CampaignCountdownComponent } from './campaign-countdown.component';

describe('CampaignCountdownComponent', () => {
  let component: CampaignCountdownComponent;
  let fixture: ComponentFixture<CampaignCountdownComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CampaignCountdownComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CampaignCountdownComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
