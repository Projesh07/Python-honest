import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MediumCategoryListComponent } from './medium-category-list.component';

describe('MediumCategoryListComponent', () => {
  let component: MediumCategoryListComponent;
  let fixture: ComponentFixture<MediumCategoryListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MediumCategoryListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MediumCategoryListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
