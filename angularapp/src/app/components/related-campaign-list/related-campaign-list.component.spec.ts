import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RelatedCampaignListComponent } from './related-campaign-list.component';

describe('RelatedCampaignListComponent', () => {
  let component: RelatedCampaignListComponent;
  let fixture: ComponentFixture<RelatedCampaignListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RelatedCampaignListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RelatedCampaignListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
