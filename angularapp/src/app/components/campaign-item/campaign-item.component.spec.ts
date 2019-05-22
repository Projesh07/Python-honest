import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CampaignItemComponent } from './campaign-item.component';

describe('CampaignItemComponent', () => {
  let component: CampaignItemComponent;
  let fixture: ComponentFixture<CampaignItemComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CampaignItemComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CampaignItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
