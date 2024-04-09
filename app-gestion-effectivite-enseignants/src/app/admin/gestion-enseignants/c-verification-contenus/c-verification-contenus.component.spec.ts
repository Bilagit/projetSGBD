import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CVerificationContenusComponent } from './c-verification-contenus.component';

describe('CVerificationContenusComponent', () => {
  let component: CVerificationContenusComponent;
  let fixture: ComponentFixture<CVerificationContenusComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CVerificationContenusComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CVerificationContenusComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
