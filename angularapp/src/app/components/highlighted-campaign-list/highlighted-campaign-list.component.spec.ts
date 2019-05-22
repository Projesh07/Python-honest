import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HighlightedCampaignListComponent } from './highlighted-campaign-list.component';

describe('HighlightedCampaignListComponent', () => {
  let component: HighlightedCampaignListComponent;
  let fixture: ComponentFixture<HighlightedCampaignListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HighlightedCampaignListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HighlightedCampaignListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
