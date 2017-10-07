import { TestBed, inject } from '@angular/core/testing';

import { ConsumeRestApiService } from './consume-rest-api.service';

describe('ConsumeRestApiService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ConsumeRestApiService]
    });
  });

  it('should be created', inject([ConsumeRestApiService], (service: ConsumeRestApiService) => {
    expect(service).toBeTruthy();
  }));
});
