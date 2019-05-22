import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UserDashboardStatComponent } from './user-dashboard-stat.component';

describe('UserDashboardStatComponent', () => {
  let component: UserDashboardStatComponent;
  let fixture: ComponentFixture<UserDashboardStatComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UserDashboardStatComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UserDashboardStatComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
