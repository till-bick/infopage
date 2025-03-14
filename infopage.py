import React from "react";
import Link from "next/link";
import { motion } from "framer-motion";

export default function Home() {
  return (
    <div className="min-h-screen bg-black text-white flex flex-col items-center justify-center p-4">
      <header className="w-full p-4 bg-gray-900 shadow-md flex justify-between items-center">
        <h1 className="text-2xl font-bold text-red-500">Projektseite</h1>
        <nav>
          <ul className="flex space-x-4 text-neon-green">
            <li><Link href="/">Home</Link></li>
            <li><Link href="/projektverlauf">Projektverlauf</Link></li>
            <li><Link href="/foerderung">Förderung</Link></li>
            <li><Link href="/about">Über uns</Link></li>
          </ul>
        </nav>
      </header>

      <main className="flex-1 flex flex-col items-center justify-center text-center">
        <motion.h2 
          className="text-4xl font-semibold text-white"
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
        >
          Willkommen auf unserer Projektseite!
        </motion.h2>
        <p className="mt-4 text-gray-300 text-lg max-w-2xl">
          Hier erfährst du alles über den aktuellen Stand unseres Vorhabens. Bleib dran!
        </p>
        <motion.button 
          className="mt-6 px-6 py-2 bg-red-500 text-black font-bold rounded-lg shadow-lg hover:bg-red-700 transition"
          whileHover={{ scale: 1.1 }}
        >
          Mehr erfahren
        </motion.button>
      </main>

      <footer className="w-full p-4 bg-gray-900 shadow-md text-center text-gray-400">
        &copy; {new Date().getFullYear()} Projektseite. Alle Rechte vorbehalten.
      </footer>
    </div>
  );
}
