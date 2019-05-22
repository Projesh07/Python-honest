import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SmallCategoryItemComponent } from './small-category-item.component';

describe('SmallCategoryItemComponent', () => {
  let component: SmallCategoryItemComponent;
  let fixture: ComponentFixture<SmallCategoryItemComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SmallCategoryItemComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SmallCategoryItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
