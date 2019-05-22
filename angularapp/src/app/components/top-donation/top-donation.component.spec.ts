import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TopDonationComponent } from './top-donation.component';

describe('TopDonationComponent', () => {
  let component: TopDonationComponent;
  let fixture: ComponentFixture<TopDonationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TopDonationComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TopDonationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
