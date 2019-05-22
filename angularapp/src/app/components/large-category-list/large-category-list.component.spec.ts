import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LargeCategoryListComponent } from './large-category-list.component';

describe('LargeCategoryListComponent', () => {
  let component: LargeCategoryListComponent;
  let fixture: ComponentFixture<LargeCategoryListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LargeCategoryListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LargeCategoryListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
