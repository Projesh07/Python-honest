import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MediumCategoryItemComponent } from './medium-category-item.component';

describe('MediumCategoryItemComponent', () => {
  let component: MediumCategoryItemComponent;
  let fixture: ComponentFixture<MediumCategoryItemComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MediumCategoryItemComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MediumCategoryItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
