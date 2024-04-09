import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CGestionProgrammesComponent } from './c-gestion-programmes.component';

describe('CGestionProgrammesComponent', () => {
  let component: CGestionProgrammesComponent;
  let fixture: ComponentFixture<CGestionProgrammesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CGestionProgrammesComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CGestionProgrammesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
