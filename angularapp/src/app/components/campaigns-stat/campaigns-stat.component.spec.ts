import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CampaignsStatComponent } from './campaigns-stat.component';

describe('CampaignsStatComponent', () => {
  let component: CampaignsStatComponent;
  let fixture: ComponentFixture<CampaignsStatComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CampaignsStatComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CampaignsStatComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
