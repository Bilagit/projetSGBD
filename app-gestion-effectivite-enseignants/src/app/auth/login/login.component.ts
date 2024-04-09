/*import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  form : any = {
    email : null,
    password : null
  }

  constructor() {}
  ngOnInit(): void {
      
  }
  onSubmit() {
    console.log(this.form)
  }
}*/

// login.component.ts

import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  email: string = '';
  password: string = '';
  selectedProfile: string = '';

  constructor(private router: Router) {}

  onSubmit(): void {
    // Validation des informations de connexion
    if (this.isValidEmail(this.email) && this.password === 'admin' && this.selectedProfile !== '') {
      // Redirection vers le profil approprié
      if (this.selectedProfile === 'étudiant') {
        this.router.navigate(['/profil-etudiant']);
      } else if (this.selectedProfile === 'enseignant') {
        this.router.navigate(['/profil-enseignant']);
      }
    } else {
      // Affichage d'un message d'erreur si les informations de connexion sont incorrectes
      alert('Adresse email, mot de passe ou profil incorrect(s). Veuillez réessayer.');
    }
  }

  isValidEmail(email: string): boolean {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@esp\.sn$/;
    return emailRegex.test(email);
  }
}

