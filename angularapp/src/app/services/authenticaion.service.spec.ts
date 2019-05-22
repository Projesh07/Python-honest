import { TestBed, inject } from '@angular/core/testing';

import { AuthenticaionService } from './authenticaion.service';

describe('AuthenticaionService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [AuthenticaionService]
    });
  });

  it('should be created', inject([AuthenticaionService], (service: AuthenticaionService) => {
    expect(service).toBeTruthy();
  }));
});
