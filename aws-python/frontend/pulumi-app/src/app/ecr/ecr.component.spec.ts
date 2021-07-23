import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EcrComponent } from './ecr.component';

describe('EcrComponent', () => {
  let component: EcrComponent;
  let fixture: ComponentFixture<EcrComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EcrComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EcrComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
