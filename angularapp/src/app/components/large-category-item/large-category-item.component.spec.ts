import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LargeCategoryItemComponent } from './large-category-item.component';

describe('LargeCategoryItemComponent', () => {
  let component: LargeCategoryItemComponent;
  let fixture: ComponentFixture<LargeCategoryItemComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LargeCategoryItemComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LargeCategoryItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
