import { TestBed } from '@angular/core/testing';

import { EcrService } from './ecr.service';

describe('EcrService', () => {
  let service: EcrService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EcrService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
