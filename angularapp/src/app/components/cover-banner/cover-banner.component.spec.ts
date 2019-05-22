import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CoverBannerComponent } from './cover-banner.component';

describe('CoverBannerComponent', () => {
  let component: CoverBannerComponent;
  let fixture: ComponentFixture<CoverBannerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CoverBannerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CoverBannerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
