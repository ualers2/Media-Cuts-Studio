// src/utils/previewQueue.ts
let maxConcurrency = 4;
let running = 0;
const queue: Array<() => void> = [];

/**
 * Ajusta concorrência (opcional)
 */
export function setMaxConcurrency(n: number) {
  maxConcurrency = Math.max(1, Math.floor(n));
}

/**
 * Executa a função `fn` respeitando a concorrência global.
 */
export function runWithLimit<T>(fn: () => Promise<T>): Promise<T> {
  return new Promise((resolve, reject) => {
    const run = async () => {
      running++;
      try {
        const res = await fn();
        resolve(res);
      } catch (e) {
        reject(e);
      } finally {
        running--;
        const next = queue.shift();
        if (next) next();
      }
    };

    if (running < maxConcurrency) {
      run();
    } else {
      queue.push(run);
    }
  });
}
