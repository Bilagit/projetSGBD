import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CSuiviEnseignementsComponent } from './c-suivi-enseignements.component';

describe('CSuiviEnseignementsComponent', () => {
  let component: CSuiviEnseignementsComponent;
  let fixture: ComponentFixture<CSuiviEnseignementsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CSuiviEnseignementsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CSuiviEnseignementsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
