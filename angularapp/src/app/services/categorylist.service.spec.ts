import { TestBed, inject } from '@angular/core/testing';

import { CategorylistService } from './categorylist.service';

describe('CategorylistService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [CategorylistService]
    });
  });

  it('should be created', inject([CategorylistService], (service: CategorylistService) => {
    expect(service).toBeTruthy();
  }));
});
