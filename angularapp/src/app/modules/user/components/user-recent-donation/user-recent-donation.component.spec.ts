import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UserRecentDonationComponent } from './user-recent-donation.component';

describe('UserRecentDonationComponent', () => {
  let component: UserRecentDonationComponent;
  let fixture: ComponentFixture<UserRecentDonationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UserRecentDonationComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UserRecentDonationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
