// -------------------------------------------------------------------------------------------------
// Interfaces

export interface WriterData {
  name: string;
  email: string;
  scopes: string[];
}


// -------------------------------------------------------------------------------------------------
// Singleton

export const writerDataSingleton = (function () {

  let writerData: WriterData;
  function createInstance() { return <WriterData>{}; }
  return {
    getInstance: function () {

      if (!writerData)
        writerData = createInstance();
      return writerData;

    },
    i: function () {

      if (!writerData)
        writerData = createInstance();
      return writerData;

    },
  };

})();